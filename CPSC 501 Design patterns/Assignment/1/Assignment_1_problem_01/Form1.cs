namespace StudentApp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnTestStudent_Click(object sender, EventArgs e)
        {
            try
            {
                Student s1 = new Student();
                s1.Id = 1234;
                s1.Test1 = 89;
                s1.Test2 = 91;
                string grade = s1.ComputeGrade();
                MessageBox.Show(grade);

                //second student obj
                Student s2 = new Student();
                s2.Id = 00986;
                s2.Test1 = 5;
                s2.Test2 = 13;
                string grade2 = s2.ComputeGrade();
                MessageBox.Show(grade2);
            }
            catch (Exception ex) 
            { 
                MessageBox.Show(ex.Message); 
            }
        }

        private void btnTestGrad_Click(object sender, EventArgs e)
        {
            GradStudent gs1 = new GradStudent();
            gs1.Test1 = 89;
            gs1.Test2 = 91;
            string grade = gs1.ComputeGrade();
            MessageBox.Show(grade);
        }

        private void btnPoly_Click(object sender, EventArgs e)
        {
            Student st = new GradStudent(); //polymorphism a derived class can be of type base class
            st.Test1 = 89;
            st.Test2 = 91;
            string grade = st.ComputeGrade();
            MessageBox.Show(grade);

            //string greeting = st.Greet(); 
            //because st is of student type/student class and doesnt have greet in it
            Type tp = st.GetType();
            
            //Accessing greeting from student directly fails because the type is Student class
            //st.Greeting()

            //type cast student type object into gradstudent
            if (tp.Name == "GradStudent")
            {
                GradStudent gt = (GradStudent)st;
                MessageBox.Show(gt.Greet());
            }
        }
    }
}