using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BuilderPattern
{
    internal class StudentGradeReportDirector //injection of builder and order of building 
    {
        //injecting the build in the director's constructor 
        private readonly IStudentReportBuilder _studentGradeReportBuilder;
        public StudentGradeReportDirector(IStudentReportBuilder studentGradeReportBuilder)
        {
            _studentGradeReportBuilder = studentGradeReportBuilder;
        }
        public void BuildStudentsGradeReport() // order in which components will be built
        {
            _studentGradeReportBuilder.BuildHeader();
            _studentGradeReportBuilder.BuildBody();
            _studentGradeReportBuilder.BuildFooter();
        }
    }
}
