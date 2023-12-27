using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BuilderPattern
{
    internal interface IStudentReportBuilder
    {
        void BuildHeader();
        void BuildBody();
        void BuildProgress();
        void BuildFooter();
        StudentsReport GetReport();
    }
}
