# Code Wars Binary Addition
# Final solution

def add_binary(a,b):
    sum = a+b
    full_num = []
    place_dict = {}
    for i in range(1000):
	    new_place = 2**i
	    place_dict[new_place]= '0'
    for place,value in sorted(place_dict.items(), reverse = True):
    	if sum >= place:
            value = '1'
            sum = sum -place
        full_num.append(value)
    result = ''.join(full_num)
    no_lead_zero_result = result.lstrip('0')
    return no_lead_zero_result
            
			
'''
Basic tests
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Random tests
Testing for 1 + 1
Test Passed
Testing for 548502613686579783441927 + 616300494505088606956478
Test Passed
Testing for 126395148248298736 + 508769679208344520
Test Passed
Testing for 86986889113113708970246704187 + 55686009244237739487781887632
Test Passed
Testing for 336487023501632518141799617853 + 888693947743069647833329316838
Test Passed
Testing for 901 + 196
Test Passed
Testing for 9402 + 3227
Test Passed
Testing for 318356395555 + 54688540559392
Test Passed
Testing for 8691954731318004 + 7488957040247430
Test Passed
Testing for 998955444016712080306960 + 564473672749656299163340
Test Passed
Testing for 8887571915771 + 37381508212812
Test Passed
Testing for 512770783 + 786997431
Test Passed
Testing for 803817342464314606 + 694877787187061932
Test Passed
Testing for 104077707932203893369098408402 + 179054444974724258805912501519
Test Passed
Testing for 708 + 634
Test Passed
Testing for 789742674279543 + 696408286730079
Test Passed
Testing for 97765018247652744343 + 28962157116783773034
Test Passed
Testing for 775584363691083921428 + 712003252975998188249
Test Passed
Testing for 378677856611 + 157363466412
Test Passed
Testing for 9731165251371293565255003741 + 4632848574718706767224512700
Test Passed
Testing for 798724726180684530 + 260435067378379206
Test Passed
Testing for 75404857175358035459550 + 93350772664648584271571
Test Passed
Testing for 98079947417332385897297987 + 66171809023894696193029854
Test Passed
Testing for 64471251735994 + 50908252865728
Test Passed
Testing for 897908219005411860630 + 9332344819195069477957
Test Passed
Testing for 1 + 0
Test Passed
Testing for 40729544456911720563 + 94064152129516884784
Test Passed
Testing for 276816085744584114606279257 + 746195555323225166881900764
Test Passed
Testing for 19143277299496299597742 + 59202879972585535905317
Test Passed
Testing for 58769650528378884043 + 58819076570285966070
Test Passed
Testing for 35188766811205666757179034341 + 20442673713935884499871975037
Test Passed
Testing for 540524 + 740330
Test Passed
Testing for 898020179413514141 + 416072915493059406
Test Passed
Testing for 2643460 + 9407259
Test Passed
Testing for 541649941720804108264544 + 806296797236927181204047
Test Passed
Testing for 867878326363824785289745 + 101227296735333076894367
Test Passed
Testing for 6 + 32
Test Passed
Testing for 97079554475777887875532436939930 + 880005003482734554947268806731
Test Passed
Testing for 612124 + 18625
Test Passed
Testing for 202973901986087866310070 + 974215379021059005074526
Test Passed
50 Passed
0 Failed
0 Errors

Process took 295ms to complete
'''