# Puzzle:            https://adventofcode.com/2023/day/17
# Video explanation: https://youtu.be/tW-ZZ2gjVC0

# 1. part - Directing the crucible from the lava pool to the machine parts factory, 
#           what is the least heat loss it can incur?
import sys
from collections import defaultdict
from queue import PriorityQueue


text = '''
242222212342422142122142541122345431421646146551526551645351642256336425452375724453446342512663131362114632112553214351513513213512432214243
344311323444232425352133234543124311663241216143232411356572674727626234525231174211112663321652166626453336245433325354234442222154121211413
242434212323545545453441134342366556136636332566113324233324376224276643474655253655517532443644443152431636646225413341321221332213111121314
223441233235353323413135222142333333424252661224115211357233263574263636261213523426673347772165434263652132153232435425314244432452144143132
134313142111242532155351452444566446251243414624652716551736762747136154651662254666453636766563331421625366451536451144222544122341255341434
131433432511152341445413612521635665641233514374171625256743656374237625771532175616735472774267276165552312631456566232322524332131122441242
234223423131414321235265221261152264433454725165412365233364323642232436741465127431125546544764555577243421146423444622632252444241245333131
124344152333441111326543312455325256513256353155177212631356133164173171531165476134614715262561223576135153231552411356263114414421234514234
234142111542345541346313446466135516442344741161745764244477571274763254212645616142161143246313552752515321646333234362662143322455351233112
211325134211431535554351546623546326346513431677761177127126112342342347344644711747227311366171675546167523534614442446322435212332323452243
414421131551252346524646462151561374627625511443354347144543521573852757811331725476122554377654722565254421544424123646532336331353145114424
211352555253311142136526213142216633157344255654731541271157527581848722245755436614827415534537161762731362223321322551252234452335213132512
335221211435534326613512166154354742522144716357467675748485781232237631566553661714775587664414136311552216321713652436213644512445241112554
542511534233511123663533611543532771446372462431657812418524411142324557441525876547262811752636117143512671427144464425333655165553252314211
345344353555314662564414362151663241345333535113642125564722781264468324336431327532351615874576241123777721751571266332612363432151133453543
552315214132363316652665466322546172456736777277866776583523813345676144634325833215277854663614155335143561612377241664231442512521243153252
434444524452553151253622112744177337414276278876776685778466343767587774621668576631383315263186425776567712146672767523531631614313233314211
244513412164431644532124156311766461417215552551441867533337752544745813378532563554525618284247485735462367246552516124564523232626652152224
214141542166515222352511744434132441764364548654541557835143586555487118362685723678215835474363864678536364222676756113243523441464545232434
124442235433466454342332231764226657544533638348858715441711472674653733324467284784614853652275132325173631434231115765334511165652454324151
121433554154353225432462741677554466778211587161513274466562435137575289152354861285571162657625134355346144272636661226755564454435623314431
241452152426254131144314326266671421343467557317156358635347227195561232949561999626188332744355388128854686732157225436354436255351445414155
225311414653355324355653273473533684416427352747535316468698216357875137972459643816154482113451174864836462325725425446411564561363254515342
124253516314312413263461616175471351188137782751771376245356857833241856395463237745825931327573828428824354257461137444461146416412434523345
252545364125313334556117211423727482447364554751166587529515248482811983414866171326794362465215568382242481646354451227675455564261632652411
233126342145266216133363545653541441224653332865236647129191753221275846126641869739176118942838218675375558683655135145635323212134623614531
343424146256413457733143721712771353673173122759855956328975818324537637657251653586984589259244583412724773748362714242511733162412144256365
523312362262625325167574635138542524613521312239769339929577196332361595268899689127474744937546872772342661335357367664345561333261124642665
314136623534443411332253644134567223435457145161828253818888375265522474465622757854547225426246796722281552422831142135141746771435114225635
432545231424232326732737777136741245127255566388571264263231771853354699366857614497414897832142495835261632341284314414777454473734643621521
144411424343433513222455113612882711246723337871893431861922171851737581246917716221298624278371816992847442216881882722542416747632521664521
145332565623421472353274388725776877546164821994351561583392594732324994675543571383291934569222914961485257436181333233773257535575126611412
341531563214227125131774455133668452888652594767733711979516325286525782848952988364765452636391458947613682563846558665733716615747511134125
441135315315266127416727335642681587624392799778134171964273989447448843546422726579924441746288678658589532656487332616737441677165341262432
113461242351725462644375486754822758761696386496915457477235222356733234845976768477656337533355912934258268265882887865376334363164254536426
451365263473342334267421233773171482886169945868916166944469872355368628472856522883995754721721728665612769425382884783641421163265365431424
142654615577215213147755823337142776644859531331333464394795896963777374432334986969675294224274639565615952141352257672531277257724713641513
465235115212657213754232612756844339241822761171327249424228779879949863272622697738725664327896815615262739236776225256272577655475641456255
215242142736355535754561257278753432345529444564395356697979264944246625574837844583822932498856646647696555348112178267114252274321157662216
261556135763363166358131267245472475458766746662757669369867564453352283228485966996596586973644643132547124433751855381253855156745357446644
452142457755125664722325271561234734517174636995659428539382562356384886458533887459747342964699764654443245118477378541245172235152744542313
115134726354112137625732856582737167619177397834363685597326986539873996686743293598939237835676459912277813383843475345425117236654532553423
122332357573235763764623343731833461298973244783556596448563283867563836364537789582566948789474554898859338646842328161363623322417235616163
431266267172113272117888236179697738975419845947436722272776838938899565345789398679396276358547238572196643787549341774111643674277624341465
246153714372445177314857772884313169283439876723286379479486799745478777945384664687642548499875624357366859119799151157824326743365114346636
215135321117277238674583367275391575218676942774976724673495658864658963336384536796797987223545956378561663965161614276182711673371557713521
361665124673112866815338815776888243613463537366232247634764964496695934374965597636856666437827559764655851919654498821438578346645474464511
662271621767631442422566656134529658684488855558894458736877876589867649693589498886536368375886233483734967556462367755243856221415533712651
131265421556446762358466826392382561589879667725956863786596697966654794983667745766885679734238629967367565561132289783333584683311726644724
634744372664422575831412196482729537444638564766776956533448333388867649464594937477737338436569679343253782417199862357386537544134537644624
335112262515527346635828245174219254353958579576898895636969399639683795964436983536395587787355455856686299466223394147841151383221141552156
142462543424723656546312118449774165653542779328454536788633968938476889856783449568936367478765559637553666737322521265673261221825617562332
617471366614374565468333759333141539966766926683455363796385395476858667987578975648978463693439444629469448971593615915477374164527546511436
317643436145458274721376791164154375372474723883576547347984534966786975958849865963595636496458967225422462172593126332786588117127575227135
146162727447574423134544266791323543524274884984894547566559566466869788465769467674979348769447779949857884715832449246355584585844344242613
622525254521254484643268372325387678623635944946999548866778688957479847897478774944759488894395786477524363319943534444552326273276614171635
427621261324226562647375314773484993856635348937934656877997465995856856689778774944589594444368588656987458967283371656223128761855756622256
273277136637413754531125298661289896925569388744758368585675978564464797599645576579685884674633943993559428491278111437665364545736662223376
246737455768712284421658113275488344793392644884786974575998874456485855745869869698868575457396484464357679668336864281642881352843337372555
151711221512357461612593386979833654253975576759897588777694487764554885696496889966567536444399964995658822342717131387543238766251232612231
167551773531318644285446228479917938656764858499833999569559458667675649444657445568859967985589366625443934259577496436525667256487731312436
175114453215863214251969993392986432678748439877969688568449998796644886679796656666548948784373777448867889992485672171135265186715561232175
734563713771264516515937312558133657885654689548369347558989587744457556795569544566847748845974755848479994594665992917928635584446247524157
665775421563374128442524891597767829323888485858985757459564579887958855956888856874765754693887639753553298244626466957947473183163216646223
616611512147761216653818153588362255386977735756634976589756449489659765759588569768557658657479873354555857293937965338236283318268751162332
451115132417858551187475849921629322994745565363938988755847447795985898665877774495699494889885664868366879833959438531294285742264815755514
623761133678313455258229493722824758685274858773558386686549596965677579969598665848884687683787583448925236645769455258291883585414142277412
251536531241315583784743791324437434343768597683544568898889465977598687565675985659954444489654954348333437532492226617849843474478615563226
622522442512348686637148148913447233525357975667855986675849455887769898975756799598795994879745674789824925368723166946323153134468844246236
746565324383683841346331429853398682934384597655587468898698765557985656665795869869579958576889836595999393275265751999381154875532446577437
276763617238136225867856868327353242946373674733346444576567955598855757889786676595856585493846645343236247635395457733516858267741437572652
563345676316375276342858168768169846876394464698567655658449786556559998666666668784987557795675493585395952839613672222821768587688741515353
633212277575717783333772143385427544288446883533943587465686969685679795986655698749466656658969363954948427848299284673253133523473136254437
231547527711274117488119425424159695994484775359935585569567855558797575555655766965468548685636849995899566952494296742286524174645272614476
634747374683148514126445383333125595986593457587865546754755969956758796979896756649555678999446446677389622763348337951947411243282244336637
132571325384565687134726987298866962243596566374665655575894769868967599887757676578976488848463835897422494698672741371956472357213346162541
326641152172222253714892858869145937766933339867698878947959999969659655669999898764589499647896354947398877246437123564597472524767471214265
253665237371543733142689591525966486963576978699633699495569958568666668979696776759799686637368479793784425569789318427688447521232555351142
736242224188412531476926198316177222498786964696533554487478675665666586956957677547545645897375944687932936794317562723421766322312713532452
436126666323672171536459944852955645572389964365949349894674988567666868885667488688854985775848969383369659559831596299588448638647232676635
453472116355582361217139437696928832554623397978943377558697476885885977989545654894444597563399768839376242324318657346384282487368672251334
264235757674215131384314428163914699994754575666954957689898787954754695575768757464585999738557365644428542366717988567773636173388755733163
455566267773124466563662741315365934938279373889537933549557476669965998994995975598498473387537656583324257399499983734157287584347643372167
354627127564236646487293855153612947743844633854378973666464758859965994578456955765578546989957778957768758892955226954682617344138276217247
557731632464664756552225288982414558585696824738855783568986678469766747786677656556746979589594674748762778871556197732213278352422355553766
332535536347122354323116957597148244276876626858673739836959787569679565885878889744686739795333949656784846758785859636248621377357112751515
436445543231365814433856995461639445754359296333583363579686846774574784494758666446898646556986492746443277853952927214234785853214176674552
345376445525346866686162889427235898295289493635335596354866778949844558679889557669783369497667596497454427995845352645416121687287435751261
546642534772276142547769576187821753534787334744739897455857474454466467958568758767954774735643723235942233454568313567161166471182177357417
464124345755536868513363989465833749246856736993538459685334895875944576565866767634359576685779626392394378848596955111158135343234543122552
454353541252247431671335133645722894876564537627773389964788979789847874585798953334698334775864848272353722391527275297585431667753725652645
653125477324576412387565387548241188729624444652363798358756356866654475856449684678634773783566428358552633623256986184451541174654522164252
266622542461776373353528672322577633258887739395963364356989836793358637495654697354633487969729599954457345285597444852562365753174564334564
253116545243342877766328173444244282967534675765955764974994573576483573384843373939694579365598633354675367388983521185661538627554436532545
311455773714476786576731578553956436644293466443794885447438795933594849847584896465446396496934729695457847778525659287361664343245353376514
266216146765624736465433769751568922559762782253236473658478354445995466374463436839439468663224696374795426488283731273723413514472337245362
362157741174377315288858372998567829826568639749289469399398873645839677595989865956684669776445323495223231782356226514882873452475757522522
264637117276537526824617242198725552592627633282285448977379747387665448844968894886875567299467627534267723911635161648481734851574474322436
646221332511246428262787114489394969755732354228986486367863686934793357899754497445877352885353678342734235399269616231282637663572523474433
164531164533144344524512663435766417947897526595566355889669695654694446479969739573336476653239376475934652372864341123764353517546223371463
631232254315672266856243344439356267226375775535624633524638337676437873795757476495737499945438748417733641556351768252612343274223722154533
263514756623525117714253231571786939413121793627295834779736437393436784693857597667599793556244787539752992626346686845158384217765362655344
461635136135265416262833818216132323187228174463677632643555866978526469376785258928636898538586299474934524713551186312371377313663522463332
112123551344173614148488112116686262797981597565657647224349553978484896592929975953788567687799378993214741916877546388155466511243551742143
446461262721466747112668361672169813454274687614673958697548833385524863323535458279467467485466244559931793954878668444228255572222131243432
636343414742225262172863211576525245879151941249922466823546462555356296632683267545934247735812752482685289516265353668145415575175165325316
462314151742456253711533233137611741974536755897869377864383386862653753889855878586668468474795245876288739857676727562177164165136754412332
366532623434354653146645825377372567781836587595356527985377272653624849968437339434739627254773452198934529634288733151725651563633632164455
665344325312542131544255574172114621293726717998595462923929395659896378388993643263743646396271754867937862138387614417821175423653762565321
645151254635474465457663178647631524669917363572829434598727933735239963948322684634379599146172821658939663387887628543544257711632636112642
352563522355462415713176323246324838257356168475658914569983264632374889229982986976672171655517225426718166328843738672764255612532636651446
444442443326655573657526333134884134721727196913138186327123899993922324637849866753967548969965518191588174244861238556535555756666623155332
516653145112651257352437577328857734884762613777719193159688473831279452328221638499243977224157448952844275263366723476567371514463336655325
132315343262545414745253753137264445275361985738896385621687577784542428967383736519116242983926718192846816571658463315326625747313625341352
416421543211213776215174554746656328111257179948529735948757777464962115755713619441413271517597537812575843467185244133764464132443422123632
236113665116254412417724717352752634751585541151413643674712699121236572648874622998894336161737115367666142464341353516435517653555142313566
344436341333161572423161432355314625221255643479964171358231331251983373112634677722754823994834453445882132746355367731742476663556424526125
554514425551553557745261143517476684164276758727149752935237539617329657536884189499538334599626471575688667621735354165452533252625236565441
242431122364616515222122244117361867378163487148764691253756588526333342321925516136229727278581446754118872635243472136653347454351165332544
234234314122562264466627212174212123586335446387366245121149651177674983676929357572545865263656686474328466861672446254315145452234215222145
244223133345624451235264275317311124753524146233324854743629912139529887225248143447125376623764746352868755642714615157243464164256323422425
231335251142341225215631177646444655365542746246776254777831538784793676929893373517282613371855386477287772154214241126471133242143333522552
431251256151242461661223265311775247461738275348833157336655356132145734455413514613723334776866653762736565477226244534255341321162621131314
144514353251536161611337343355312655165185444625533713244748827518286351466836575263673324116132317331685671254514534762222343542514311315552
344532115432261541216255132425234571275123838265617753658553336546515584747173286357712488817134525488836526755772127135533515555345163333253
351513315552464521632254365236175314473561564414627135716358832883433468156162157758875743135815715767727163647742156765114231436321651552144
512552511322123331651324463644232266643477718761423874836433345868717462123813525543152651836316478656431223171332337422243232412525515241153
242151412331541554452242141654777264362231545656427845352162537724363255434182856483783886131242125513462147531355565256145221613444151513125
225315123154463666322351541355655366225224533433263856661841468876212627367281424663142783877641511524162471521212252662141465125133432221221
221545323225151453422344435417253373767325363671217478525342662811747851625388438133386364746654426652536442524241146354364134356321252351522
144114114455151542643361412541635672477513145755111642683184245782187467285125463875837862637122463116322362232754321231353222553114153154122
145253154233124221525413246621164542533755261666216516531251524556357618833511561124246623416245634131675637253631356124361356244523321351553
313254132222452212625333252343156144265165177543637641241565447627886563471312416447326226575477142344334776316611363546251626453322135241354
341245323314115332662335232363333415334574656442634471231762463543571512621371673732722137224752653164667444226341345612222662212424123431132
124411411423155433512215521351165453117255261147541676514725125554225737246645616454172715662744146551171212122333512214465412242412523414421
411444313125511212322465364164142215135544153411357372667426562277723532276525452227774231375113176753556112214145116225541211555534421535132
331334315545431145211345565335451434522122444146236476432764262234112134643716741441177571143726324475245331516614545365222315554541335212423
112441221212134131215112541121144612352542211123317722671141475515326712643627523223657251511456173163412113266214151412242443315255515211142
222312312324443421333313552523166415341364556152647665242151545257175424344355437562454365153334263226563123555242621153345344553424344133234
321233113315131415431521343432541534655564615522417521435421215751312747273265434213632165733353321213232114445423132421522554531415452424443
243442133422335213523311433541461161212352253653661644371165173467763311477373666374437216413115424643326363462415461144445112354124313122324
'''

text_test = '''
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
'''

text_test2 = '''
111111111111
999999999991
999999999991
999999999991
999999999991
'''


def read(text):
    res = []
    for line in text.split('\n'):
        if not line:
            continue

        res.append(tuple(int(i) for i in line))

    return res



# 1. and 2. part combined
import sys
from collections import defaultdict
from queue import PriorityQueue

RIGHT, LEFT, UP, DOWN = (1, 0), (-1, 0), (0, -1), (0, 1)
CRUCIBLE_TURNS = {RIGHT: [UP, DOWN], LEFT: [UP, DOWN], UP: [LEFT, RIGHT], DOWN: [LEFT, RIGHT]}


def get_min_heat_loss(heat_loss_map, blocks_before_turn, max_in_direction):
    # distance is in this case cumulative heat loss
    dist = defaultdict(lambda: defaultdict(lambda: sys.maxsize))
    dist[(0, 0)][RIGHT] = 0
    dist[(0, 0)][DOWN] = 0
    dist[(0, 0)][UP] = 0
    dist[(0, 0)][LEFT] = 0

    # Dijkstra's algorithm
    pq = PriorityQueue()
    pq.put((0, (0, 0), RIGHT))
    pq.put((0, (0, 0), DOWN))

    while not pq.empty():
        heat_loss, position, direction = pq.get()

        if heat_loss > dist[position][direction]:
            continue

        # find positions where the crucible can turn
        x, y = position
        for block in range(max_in_direction):
            # move in the direction
            x, y = x + direction[0], y + direction[1]

            # out of bounds check
            if x < 0 or x >= len(heat_loss_map[0]) or y < 0 or y >= len(heat_loss_map):
                break

            # cumulate heat losses
            heat_loss += heat_loss_map[y][x]

            # crucible needs to move a minimum of N blocks in that direction before it can turn
            if block < blocks_before_turn:
                continue

            # turn the crucible
            for new_dir in CRUCIBLE_TURNS[direction]:
                if heat_loss < dist[(x, y)][new_dir]:

                    dist[(x, y)][new_dir] = heat_loss
                    pq.put((heat_loss, (x, y), new_dir))

    return min(dist[(len(heat_loss_map[0]) - 1, len(heat_loss_map) - 1)].values())


def solve_test(text):
    heat_loss_map = [list(map(int, line.strip())) for line in text.split('\n') if line]

    print(get_min_heat_loss(heat_loss_map, 0, 3))
    print(get_min_heat_loss(heat_loss_map, 3, 10))

solve_test(text)