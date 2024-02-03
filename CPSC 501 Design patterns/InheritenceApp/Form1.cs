namespace InheritenceApp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnTest_Click(object sender, EventArgs e)
        {
            //VolumeShape volumeShape = new VolumeShape();
            VolumeShape v1 = new Cylinder();
            v1.Radius = 10;
            //v1.Height - getting issues here because the compiler checks the type first/the type is volumeshape with no length property
            //solution
            Cylinder c1 = (Cylinder)v1;
            c1.Height = 34;
            double vol = v1.ComputeVolume();
            MessageBox.Show("Volume is  " +  vol +" "+ "cubic units");
        }
    }
}