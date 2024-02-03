using DBStudentApp_1174066.DataLayer;
using DBStudentApp_1174066.Models;

namespace DBStudentApp_1174066
{
    public partial class fmStudent : Form
    {
        public fmStudent()
        {
            InitializeComponent();
        }

        private void fmStudent_Load(object sender, EventArgs e)
        {
            IRepository irep = new Repository();
            List<Course> courseList = irep.GetAllCourses();
            cmbCourses.DataSource = courseList;
            cmbCourses.DisplayMember = "CourseNum";
            cmbCourses.ValueMember = "CourseNum";
            cmbCourses.Refresh();
        }

        private void cmbCourses_SelectedIndexChanged(object sender, EventArgs e)
        {
            string courseNum = cmbCourses.SelectedValue.ToString();
            //MessageBox.Show(courseNum);
            IRepository irep = new Repository();
            var EList = irep.GetEnrollment(courseNum);
            dg1.DataSource = EList;
            dg1.Refresh();
        }
    }
}