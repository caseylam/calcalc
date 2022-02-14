from unittest import TestCase
import CalCalc

class TestStuff(TestCase):
    def test0():
        assert abs(4. - CalCalc.calculate('2**2')) < 0.001
    
    def test1():
        assert abs(206. - CalCalc.calculate('how many bones in the human body', return_float=True)) < 0.001
        
    def test2():
        assert abs(12. - CalCalc.calculate('convert 1 feet to inches', return_float=True)) < 0.001
        
    def test3():
        assert abs(2.e204 - CalCalc.calculate('10e3*2e200')) < 10.e203
        
    def test4():
        assert abs(7.3459e22 - CalCalc.calculate('mass of the moon in kg', return_float=True)) < 10.e21
        
    def test5():
        assert abs(100. - CalCalc.calculate('water boiling point in celsius', return_float=True)) < 1
    
