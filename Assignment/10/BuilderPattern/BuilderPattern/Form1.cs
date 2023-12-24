namespace BuilderPattern
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        private void Form1_Load(object sender, EventArgs e)
        {

        }
        private void btnTestGradeReport_Click(object sender, EventArgs e)
        {
            //creating the list of students
            var SList = new List<Student>
            {
                new Student { Id = 12341, Major = "CS", Name = "William Baker", Test1 = 85, Test2 = 91 },
                new Student { Id = 12342, Major = "EE", Name = "Sally Simpson", Test1 = 81, Test2 = 88 },
                new Student { Id = 12343, Major = "ME", Name = "Mark Mathews", Test1 = 89, Test2 = 95 },
            };
            //generating report
            var builder = new StudentGradeReportBuilder(SList);
            var director = new StudentGradeReportDirector(builder); // ingesting StudentGradeReportBuilder to build a report
            director.BuildStudentsGradeReport();
            var report = builder.GetReport();
            MessageBox.Show(report.ToString());
        }

        private void btnTestProgressReport_Click(object sender, EventArgs e)
        {
            //creating the list of students
            var SList = new List<Student>
             {
             new Student { Id= 12341, Major="CS", Name="William Baker", Test1=85},
             new Student { Id= 12342, Major="EE", Name="Sally Simpson", Test1=95},
             new Student { Id= 12343, Major="ME", Name="Mark Mathews", Test1=65},
             };
            //generating report
            var builder = new StudentProgressReportBuilder(SList);
            var director = new StudentProgressReportDirector(builder); // ingesting StudentGradeReportBuilder to build a report
            director.BuildStudentsProgressReport();
            var report = builder.GetReport();
            MessageBox.Show(report.ToString());
        }
    }
}
