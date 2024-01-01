namespace GradingApp
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

        private void btnProcessGrades_Click(object sender, EventArgs e)
        {
            try
            {
                string inputFile = "F:/CPSC501/data/StudentData.txt";
                string outputFile = "F:/CPSC501/data/StudentGrades.txt";
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