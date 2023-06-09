import sys
import os
from xml.dom import minidom
from xml.parsers.expat import ExpatError


def read_coverage_jacoco(output_file_dir_path):
    if not os.path.isfile(output_file_dir_path + '/coverage.xml'):
        print "No such output file. Please check your file path."
        return 0

    try:
        # see the format of coverage report generated by Jacoco in xml
        xmldoc = minidom.parse(output_file_dir_path + '/coverage.xml')
        counters = xmldoc.getElementsByTagName('counter')
        line_coverage = 0
        for counter in counters:
            type_name = counter.getAttribute('type')
            if type_name == 'LINE':
                missed_lines = int(counter.getAttribute('missed'))
                covered_lines = int(counter.getAttribute('covered'))
                line_coverage = covered_lines * 1.0 / (missed_lines + covered_lines)

        print "missed line number: " + str(missed_lines)
        print "covered line number: " + str(covered_lines)
        print "-----------"
        print "current jacoco line coverage rate : " + str(line_coverage)
        print "-----------"
    except ExpatError:
        print "parse xml error!"
        return 0

def main():
    output_file_path = sys.argv[1]
    read_coverage_jacoco(output_file_path)

if __name__ == '__main__':
        main()