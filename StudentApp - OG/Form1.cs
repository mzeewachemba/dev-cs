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
                s1.Test1 = 185;
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
            catch (Exception ex) { MessageBox.Show(ex.Message); }   
        }
    }
}