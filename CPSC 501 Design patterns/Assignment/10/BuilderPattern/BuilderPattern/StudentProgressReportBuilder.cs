using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BuilderPattern
{
    internal class StudentProgressReportBuilder : IStudentReportBuilder
    {
        private StudentsReport _studentReport;
        private List<Student> SList;
        public StudentProgressReportBuilder(List<Student> students)
        {
            SList = students;
            _studentReport = new StudentsReport();
        }
        public void BuildBody()
        {
            throw new NotImplementedException(); // no body in progress report
        }
        public void BuildFooter()
        {
            _studentReport.FooterPart = "\n---------Fall Semester 2023----------";
        }
        public void BuildHeader()
        {
            _studentReport.HeaderPart = "\nProgress Report Date: " +
           DateTime.Now.ToShortDateString() + "\n\n";
        }
        public void BuildProgress()
        {
            string out1 = "";
            //loop through students to generate their progress report
            foreach (Student st in SList)
                if (st.Test1 > 70)
                    out1 += $"{st.Id}\t{st.Name}\t{st.Major}\t{st.Test1} - Satisfactory\n";
                else
                    out1 += $"{st.Id}\t{st.Name}\t{st.Major}\t{st.Test1} - UnSatisfactory\n";
            _studentReport.BodyPart = out1;
        }
        public StudentsReport GetReport()
        {
            //Clear();
            return _studentReport;
        }
        private void Clear() => _studentReport = new StudentsReport();
    }
}
