using GraddingAppAssignment2;

namespace GraddingAppAssignment2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnProcessGrades_Click(object sender, EventArgs e)
        {
            try
            {
                string inputFile = "F:/CPSC501/data_2/StudentData.txt";
                string outputFile = "F:/CPSC501/data_2/StudentGrades.txt";
                ProcessGrades pg = new ProcessGrades();
                pg.ReadStudentData(inputFile);
                pg.ProcessAndWriteGrades(outputFile);
                MessageBox.Show("Grades processed, examine file " + outputFile);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }
    }
}