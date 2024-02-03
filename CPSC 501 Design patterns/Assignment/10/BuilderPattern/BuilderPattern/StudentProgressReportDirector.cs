using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BuilderPattern
{
    internal class StudentProgressReportDirector
    {
        //injecting the build in the director's constructor 
        private readonly IStudentReportBuilder _studentProgressReportBuilder;
        public StudentProgressReportDirector(IStudentReportBuilder studentProgressReportBuilder)
        {
            _studentProgressReportBuilder = studentProgressReportBuilder;
        }
        public void BuildStudentsProgressReport() // ordering the methods
        {
            _studentProgressReportBuilder.BuildHeader();
            _studentProgressReportBuilder.BuildProgress();
            _studentProgressReportBuilder.BuildFooter();
        }
    }
}
