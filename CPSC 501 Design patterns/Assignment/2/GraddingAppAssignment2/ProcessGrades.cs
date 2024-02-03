using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GraddingAppAssignment2
{
    internal class ProcessGrades : IProcessGrades
    {
        public List<Student> STList { get; set; } = new List<Student>();

        public void ProcessAndWriteGrades(string outFileName)
        {
            StreamWriter sw = new StreamWriter(outFileName);
            try
            {
                STList.Sort();//initiating comparison before printing the grades
                foreach (Student st in STList)
                {
                    string grade = st.ComputeGrade(); 
    
                    sw.WriteLine(st.ID + "\t" + grade);
                }
                sw.Close();
            }
            catch
            {
                throw; //send error to the caller
            }

            finally // close the stream for this io
            {
                sw.Close();
            }

        }

        public void ReadStudentData(string inputFileName)
        {
            try
            {
                STList.Clear(); 
                StreamReader sr = new StreamReader(inputFileName);
                string sline = sr.ReadLine();
                while (sline != null)
                {
                    Student st = null; 
                    string[] parts = sline.Split(new char[] { '\t' });
                    if (parts.Length == 6) 
                    {
                        if (parts[3].ToUpper() == "UNDERGRAD")
                        {
                            st = new UnderGradStudent(int.Parse(parts[0]), parts[1],
                            parts[2], int.Parse(parts[4]), int.Parse(parts[5]));
                        }
                    }
                    if (parts.Length == 7) // for grad student
                    {
                        if (parts[3].ToUpper() == "GRADUATE")
                        {
                            st = new GradStudent(int.Parse(parts[0]), parts[1],
                            parts[2], int.Parse(parts[4]), int.Parse(parts[5]),
                           parts[6]);
                        }
                    }
                    if (parts.Length == 9) // for Phd student
                    {
                        if (parts[3].ToUpper() == "PHDCPSC")
                        {
                            st = new PhdStudent(int.Parse(parts[0]), parts[1],
                            parts[2], int.Parse(parts[5]), int.Parse(parts[6]),
                           parts[7], parts[8]);
                        }
                    }
                    if (st != null)
                        STList.Add(st); // adding student to the list
                    sline = sr.ReadLine(); // take next line
                }
            }
            catch
            {
                throw; //send errors to the caller
            }
        }
    }
}
