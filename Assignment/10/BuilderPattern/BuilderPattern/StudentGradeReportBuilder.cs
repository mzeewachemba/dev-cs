using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BuilderPattern
{
    internal class StudentGradeReportBuilder : IStudentReportBuilder
    {
        private StudentsReport _studentGradeReport;
        private List<Student> SList;
        public StudentGradeReportBuilder(List<Student> students)
        {
            SList = students;
            _studentGradeReport = new StudentsReport();
        }
        public void BuildBody()
        {
            string out1 = "";
            //loop through the list of student and build their grade report
            foreach (Student st in SList)
                out1 += $"{st.Id}\t{st.Name}\t{st.Major}\t{st.ComputeGrade()}\n";
            _studentGradeReport.BodyPart = out1;
        }
        public void BuildFooter()
        {
            _studentGradeReport.FooterPart = "\n---------Fall Semester 2023----------";
        }
        public void BuildHeader()
        {
            _studentGradeReport.HeaderPart = "\nGrade Report Date: " +
           DateTime.Now.ToShortDateString() + "\n\n";
        }
        public void BuildProgress()
        {
            throw new NotImplementedException();
        }
        public StudentsReport GetReport() // final overall report
        {
            //Clear();
            return _studentGradeReport;
        }
        private void Clear() => _studentGradeReport = new StudentsReport();
    }
}
