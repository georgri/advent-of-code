from collections import defaultdict

text = '''
%db -> cq
%rj -> gp, nd
%ff -> bk
%rc -> gp
%bk -> tv
%xz -> tf, bn
%gs -> bn
%ps -> rs, gp
%jr -> gp, cg
&pm -> vf
%pn -> pp, rt
%nv -> jr
%rs -> nv
%kz -> mj
%nd -> rc, gp
%nm -> rt, db
%dg -> rt, xl
%vg -> gn
%hc -> vr
%ft -> lf, bn
%mj -> hc, cz
%vb -> ft
%qd -> cz, sz
%pp -> rt
%cq -> rt, vg
%sr -> vb
%lf -> vx, bn
%lh -> pn, rt
%ls -> sl, cz
%tv -> gp, rj
%tf -> sr, bn
&mk -> vf
%bs -> rt, lh
%vx -> bn, gs
&bn -> fs, bv, vb, mk, sr, bz, cf
%rr -> ls
%bv -> xz
%hp -> bs, rt
&pk -> vf
%cg -> rq
%gn -> rt, dg
&cz -> hc, kz, rr, hf, sh
%sl -> cz, kz
broadcaster -> sh, nm, ps, fs
%cf -> bv
&vf -> rx
&rt -> pk, xl, nm, vg, db
%xl -> hp
%sh -> rr, cz
%bz -> cf
%fz -> dn, cz
&gp -> rs, nv, pm, cg, ff, bk, ps
%fs -> bz, bn
&hf -> vf
%vr -> cz, qd
%rq -> gp, ff
%sz -> cz, fz
%dn -> cz
'''

text_test1 = '''
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
'''

text_test2 = '''
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
'''


def read(text):
    res = dict()

    for line in text.split('\n'):
        if not line:
            continue

        module, connected = line.split(' -> ')
        conn_list = tuple(connected.split(', '))
        if module == 'broadcaster':
            res[module] = ('broadcaster', conn_list)
        else:
            res[module[1:]] = [module[0], conn_list]

    return res


print(read(text_test1))


def init_modules_states(modules):

    flip_flops = dict()
    conjunctions = dict()
    for mod_name, (mod_type, _) in modules.items():

        if mod_type == '%':
            flip_flops[mod_name] = 0 # all flip-flops are off
        elif mod_type == '&':
            conjunctions[mod_name] = dict()

    for mod_name, (mod_type, connected_to) in modules.items():
        for connected_name in connected_to:
            if connected_name in conjunctions:
                # 0 is low, 1 is high
                conjunctions[connected_name][mod_name] = 0

    return flip_flops, conjunctions


def process_broadcaster(modules, module_name, signal):
    # broadcast signal to all neighbors
    _, adj = modules[module_name]
    return [(module_name, mod, signal) for mod in adj]


def process_flip_flop(modules, flip_flops, module_name, signal):
    if signal == 1:
        return [] # ignore high signal

    # flip the state
    state = flip_flops[module_name]
    state = 1 - state # 0 => 1, 1 => 0
    flip_flops[module_name] = state

    return process_broadcaster(modules, module_name, state)


def process_conjunction(modules, conjunctions, from_module, module_name, signal):
    # update memory on input
    conjunctions[module_name][from_module] = signal

    send_pulse = 1
    # check if high on all inputs
    if all(s == 1 for s in conjunctions[module_name].values()):
        send_pulse = 0

    return process_broadcaster(modules, module_name, send_pulse)


def push_button(modules, flip_flops, conjunctions, iteration, watcher):

    low, high = 0, 0

    # 0 is low, 1 is high
    # when the button is pushed, a single low signal is sent to the broadcaster
    cur_queue = [('button', 'broadcaster', 0)]

    while cur_queue:
        next_queue = []
        for from_module, module_name, signal in cur_queue:
            if watcher == (module_name, signal):
                print("sent {} from {} on iteration {}".format(watcher, from_module, iteration))
            if signal == 0:
                low += 1
            else:
                high += 1
            if module_name == 'broadcaster':
                next_steps = process_broadcaster(modules, module_name, signal)
                next_queue.extend(next_steps)
            if module_name in conjunctions:
                next_steps = process_conjunction(modules, conjunctions, from_module, module_name, signal)
                next_queue.extend(next_steps)
            elif module_name in flip_flops:
                next_steps = process_flip_flop(modules, flip_flops, module_name, signal)
                next_queue.extend(next_steps)

        cur_queue = next_queue

    return low, high


def solve(text):

    modules = read(text)

    flip_flops, conjunctions = init_modules_states(modules)

    total_low, total_high = 0, 0
    for i in range(1000):

        cur_low, cur_high = push_button(modules, flip_flops, conjunctions, i+1, ('rx', 0))

        total_low += cur_low
        total_high += cur_high

    print(total_low * total_high)


# solve(text)



def solve2(text):

    modules = read(text)

    flip_flops, conjunctions = init_modules_states(modules)

    total_low, total_high = 0, 0
    for i in range(10000):

        cur_low, cur_high = push_button(modules, flip_flops, conjunctions, i+1, ('vf', 1))

        total_low += cur_low
        total_high += cur_high

    # print(total_low * total_high)

solve2(text)


def largest_common_divisor(a, b):
    if b == 0:
        return a
    return largest_common_divisor(b, a % b)


def least_common_denominator(a,b):
    return a*b // largest_common_divisor(a,b)



'''
sent ('vf', 1) from pm on iteration 3881
sent ('vf', 1) from mk on iteration 3889
sent ('vf', 1) from hf on iteration 4013
sent ('vf', 1) from pk on iteration 4021
sent ('vf', 1) from pm on iteration 7762
sent ('vf', 1) from mk on iteration 7778
sent ('vf', 1) from hf on iteration 8026
sent ('vf', 1) from pk on iteration 8042
'''

res = 1
for i in (3881, 3889, 4013, 4021):
    res = least_common_denominator(res, i)

print(res)

# WTF???!?!?!?!?!?!?!? 243 TRILLION
# 243548140870057





