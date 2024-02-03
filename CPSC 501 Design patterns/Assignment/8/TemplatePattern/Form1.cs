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
                @"D:\13.MSCS\repo__\dev-cs\Assignment\8\StudentData.txt",
                @"D:\13.MSCS\repo__\dev-cs\Assignment\8\StudentDataOut.txt");
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
                @"D:\13.MSCS\repo__\dev-cs\Assignment\8\StudentData.txt",
                @"D:\13.MSCS\repo__\dev-cs\Assignment\8\StudentDataOut.txt", igst);
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
