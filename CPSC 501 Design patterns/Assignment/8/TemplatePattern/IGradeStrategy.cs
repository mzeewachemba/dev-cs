using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TemplatePattern
{
    interface IGradeStrategy
    {
        string ComputeGrade(Student st);
    }
}
