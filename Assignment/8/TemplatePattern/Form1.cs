namespace TemplatePattern
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnTemplate_Click(object sender, EventArgs e)
        {
            //initialize input files and output files 
            TemplateStudent tst = new StudentProcessingViaFile(
                @"E:\2.Online MS CS\2nd Year\1st Semester\CPSC501\dev-cs\Assignment\8\StudentData.txt",
                @"E:\2.Online MS CS\2nd Year\1st Semester\CPSC501\dev-cs\Assignment\8\StudentDataOut.txt");
            tst.ReadAndProcessStudents(); //call all steps
            // process students via DB
            TemplateStudent tst2 = new StudentProcessingViaDB();
            tst2.ReadAndProcessStudents(); //will call all the steps
            MessageBox.Show("done processing..");
        }

        private void btnTemplateStrategy_Click(object sender, EventArgs e)
        {
            //SWITCHING THE Computegrade formulas
            IGradeStrategy igst = new ComputeGrade4060();
            //IGradeStrategy igst = new ComputeGrade5050();
            TemplateStudent tst = new StudentProcessingViaFile2(
                @"E:\2.Online MS CS\2nd Year\1st Semester\CPSC501\dev-cs\Assignment\8\StudentData.txt",
                @"E:\2.Online MS CS\2nd Year\1st Semester\CPSC501\dev-cs\Assignment\8\StudentDataOut.txt", igst);
            tst.ReadAndProcessStudents();
            MessageBox.Show("done..for file");

        }

        private void btnTemplateStrategyDB_Click(object sender, EventArgs e)
        {
            //SWITCHING THE Computegrade formulas
            //IGradeStrategy igst = new ComputeGrade4060();
            IGradeStrategy igst = new ComputeGrade5050();
            TemplateStudent tst = new StudentProcessingViaDB2(igst);
            tst.ReadAndProcessStudents();
            MessageBox.Show("done..for DB");
        }
    }
}
