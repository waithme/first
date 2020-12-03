import unittest
from dorrigo_mobile import dorrigo_mobile
from dorrigo_network import dorrigo_network
from dorrigo_contact import dorrigo_contact

class safe_net_tester(unittest.TestCase):

    def test1(self):
        a = dorrigo_mobile(max_contacts=5)
        n1 = dorrigo_network(name='today', signal=3, cipher='123',...)
        n2 = dorrigo_network() 
        n3 = dorrigo_network()
        net_list = [n1, n2, n3]
        tuple1 = (n1.get_network_name, "safe")
        tuple2 = (n2.get_network_name, "safe")
        tuple3 = (n3.get_network_name, "cond safe", '1','2')
        safe_list = [tuple1, tuple2, tuple3] 
        """
        target_network = Belstra, signal strength 1, network cipher AES, certified date 2020-11-20
        safe_list = 
        [
            ("FreedomNet", "safe"),
            ("GoldenDawn", "not safe"),
            ("Belstra", "cond safe", "1"),
            ("OhMyResistance", "safe"),
            ("Optocom", "cond safe", "2", "2", "1", "Belstra"),
            ("SatCom", "cond safe", "5", "0", "0", "LordHelmet"),
            ("JellyCom", "cond safe", "2", "1", "1", "GoldenDawn"),
            ("FroggyCom", "cond safe", "0", "0", "0", "", "Horseshoe", "OhMyResistance, LightningRod")
        ]
            
        available_network =    
        [FreedomNet, signal strength 5, network cipher RSA, certified date 2020-03-10
        FreedomNet, signal strength 3, network cipher Ceasar, not certified
        Belstra, signal strength 1, network cipher AES, certified date 2020-11-20
        Belstra, signal strength 5, network cipher AES, certified date 2020-10-05
        Optocom, signal strength 4, network cipher AES, certified date 2020-06-01
        Moctocom, signal strength 1, network cipher ECB, certified date 2019-04-29
        SatCom, signal strength 1, network cipher AES, certified date 1984-06-24
        JellyCom, signal strength 2, network cipher CBC, certified date 2020-10-31
        GoldenDawn, signal strength 5, network cipher StringCan, not certified]
        """
        assert a.is_safe_network(n1.get_network_name(), net_list, "2020-11-30", safe_list)==True
    
    def test2(self):
        a = dorrigo_mobile()
        n1 = dorrigo_network()
        n2 = dorrigo_network() # assume that n2.signal_strength = 2
        n3 = dorrigo_network()
        net_list = [n1, n2, n3]
        tuple1 = (n1.get_network_name, "safe")
        tuple2 = (n2.get_network_name, "safe", "2")
        tuple3 = (n3.get_network_name, "safe", "1", "1")
        safe_list = [tuple1, tuple2, tuple3]

        assert a.is_safe_network(n2.get_network_name(), net_list, "2020-11-30", safe_list)==True
    
    def test3():
        a = dorrigo_mobile()
        n1 = dorrigo_network()
        n2 = dorrigo_network() 
        n3 = dorrigo_network() # n3.signal_strength = 2 and n3.name = "FreedomNet" and n3.certificate_signed_date = "2020-12-30"
        net_list = [n1, n2, n3]
        tuple1 = (n1.get_network_name, "safe")
        tuple2 = (n2.get_network_name, "safe", "2")
        tuple3 = (n3.get_network_name, "safe", "1", "1")
        safe_list = [tuple1, tuple2, tuple3]

        assert a.is_safe_network(n3.get_network_name(), net_list, "2020-11-30", safe_list)==True
    
    def test4():
        a = dorrigo_mobile()
        n1 = dorrigo_network()
        n2 = dorrigo_network() 
        n3 = dorrigo_network() # n3.signal_strength = 2 and n3.name = "FreedomNet" and n3.certificate_signed_date = "not certified"
        net_list = [n1, n2, n3]
        tuple1 = (n1.get_network_name, "safe")
        tuple2 = (n2.get_network_name, "safe", "2")
        tuple3 = (n3.get_network_name, "safe", "1", "1")
        safe_list = [tuple1, tuple2, tuple3]

        assert a.is_safe_network(n3.get_network_name(), net_list, "2020-11-30", safe_list)==False
    
    def test5():
        a = dorrigo_mobile()
        n1 = dorrigo_network()
        n2 = dorrigo_network() 
        n3 = dorrigo_network() 
        n4 = dorrigo_network()
        net_list = [n1, n2, n3, n4]
        tuple1 = (n1.get_network_name, "safe", "1", "0", "1") # n1.signal_strength = 2 and n1.certificate_signed_date = "2021-11-30"
        tuple2 = (n2.get_network_name, "safe", "2", "0", "5", "abc")
        tuple3 = (n3.get_network_name, "safe", "1", "1" , "2", "ab", "Mary")
        tuple4 = (n4.get_network_name, "safe", "1", "0", "3", "abcd", "Jack", "abc,abcde")
        safe_list = [tuple1, tuple2, tuple3, tuple4]

        assert a.is_safe_network(n1.get_network_name(), net_list, "2020-11-30", safe_list)==True
    
    def test6():
        a = dorrigo_mobile()
        n1 = dorrigo_network() # n1.name="abc"
        n2 = dorrigo_network() # n2.signal_strength = 2 and n2.certificate_signed_date = "2021-11-30"
        n3 = dorrigo_network()
        n4 = dorrigo_network()
        net_list = [n1, n2, n3, n4]
        tuple1 = (n1.get_network_name, "safe", "1", "0", "1") 
        tuple2 = (n2.get_network_name, "safe", "2", "0", "5", "abc")
        tuple3 = (n3.get_network_name, "safe", "1", "1" , "2", "ab", "Mary")
        tuple4 = (n4.get_network_name, "safe", "1", "0", "3", "abcd", "Jack", "abc,abcde")
        safe_list = [tuple1, tuple2, tuple3, tuple4]

        assert a.is_safe_network(n2.get_network_name(), net_list, "2020-11-30", safe_list)==True
    
    def test7():
        a = dorrigo_mobile()
        n1 = dorrigo_network() # n1.name="ab"
        n2 = dorrigo_network() 
        n3 = dorrigo_network() # n3.name="FreedomNet" and n3.signal_strength = 2 and n3.certificate_signed_date = "2021-11-30" and n3.cipher="Jack"
        n4 = dorrigo_network()
        net_list = [n1, n2, n3, n4]
        tuple1 = (n1.get_network_name, "safe", "1", "0", "1") 
        tuple2 = (n2.get_network_name, "safe", "2", "0", "5", "abc")
        tuple3 = (n3.get_network_name, "safe", "1", "1" , "2", "ab", "Mary")
        tuple4 = (n4.get_network_name, "safe", "1", "0", "3", "abcd", "Jack", "abc,abcde")
        safe_list = [tuple1, tuple2, tuple3, tuple4]

        assert a.is_safe_network(n2.get_network_name(), net_list, "2020-11-30", safe_list)==False
    
    def test8():
        a = dorrigo_mobile()
        n1 = dorrigo_network() # n1.name="abcd"
        n2 = dorrigo_network() # n2.name="abc"
        n3 = dorrigo_network() # n3.name="abcde"
        n4 = dorrigo_network() # n4.signal_strength = 2 and n4.certificate_signed_date = "2021-11-30" and n3.cipher="Jack"
        net_list = [n1, n2, n3, n4]
        tuple1 = (n1.get_network_name, "safe", "1", "0", "1") 
        tuple2 = (n2.get_network_name, "safe", "2", "0", "5", "abc")
        tuple3 = (n3.get_network_name, "safe", "1", "1" , "2", "ab", "Mary")
        tuple4 = (n4.get_network_name, "safe", "1", "0", "3", "abcd", "Jack", "abc,abcde")
        safe_list = [tuple1, tuple2, tuple3, tuple4]

        assert a.is_safe_network(n2.get_network_name(), net_list, "2020-11-30", safe_list)==False
