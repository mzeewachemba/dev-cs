using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TemplatePattern
{
    internal class ComputeGrade5050 : IGradeStrategy//concrete stratergy 2
    {
        public string ComputeGrade(Student st)
        {
            string grade = "";
            double avg = 0.5 * st.Test1Score + 0.5 * st.Test2Score; //specific formular
            if (avg > 90)
                grade = "A";
            else if (avg > 85)
                grade = "A-";
            else if (avg > 80)
                grade = "B+";
            else
                grade = "B";
            return grade;
        }
    }
}
