using DBStudentApp.DataLayer;
using DBStudentApp.Models;

namespace DBStudentApp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            IRepository irep = new Repository();
            List<Course> courseList = irep.GetAllCourses();
            cmbCourses.DataSource = courseList;
            cmbCourses.DisplayMember = "CourseNum";
            cmbCourses.ValueMember = "CourseNum";
            cmbCourses.Refresh();
        }
    }
}