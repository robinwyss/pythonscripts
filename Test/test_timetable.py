import unittest
from BusTimetable import extract_departures
from testdata import timetable_html_doc, buslines_html_doc
class Test_Extractor(unittest.TestCase):

    def test_departures(self):
        departures = extract_departures(timetable_html_doc)
        self.assertEquals(departures.nextdepartures,[9, 24, 39])

    def test_timetable(self):
        departures = extract_departures(timetable_html_doc)
        self.assertEquals(departures.departuretimes, [('20', ['47']),('21', ['02', '17', '32', '47']),('22', ['02', '17', '32', '47']),('23', ['02', '17', '32', '47']), ('00', ['02', '17', '32'])])

    def test_buslines(self):
        buslines = extract_buslines(buslines_html_doc)
        self.assertEquals(buslines, [('1', 'line_25_01'),('2', 'line_25_02'),('4', 'line_25_04'),('5', 'line_25_05'),('6', 'line_25_06'),('7', 'line_25_07'),('8', 'line_25_08'),('9', 'line_25_09'),('11', 'line_25_11'),('12', 'line_25_12'),('71', 'line_25_71'),('72', 'line_25_72')])

if __name__ == '__main__':
    unittest.main()