namespace AdapterPattern
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnAdapterMath_Click(object sender, EventArgs e)
        {
            //calling the existing method via the interface, while reusing the existing code
            try
            {
                INewMath am = new AdapterMath();
                double[] A = { 3.7, 8.4, 6.3 };
                //computing avg value
                double res = am.ComputeAvgNew(A);
                //computing min value
                double resMin = am.FindMinNew(A);

                MessageBox.Show("Result for avg = " + res.ToString());

                MessageBox.Show("Result for min = " + resMin.ToString());
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        //additional behavior rounded avg
        private void btnAdapterMath2_Click(object sender, EventArgs e)
        {
            try
            {
                INewMath am = new AdapterMath();
                double[] A = { 3.7, 8.4, 6.3 };
                int res = am.ComputeAvgRound(A);
                MessageBox.Show("Result (Rounded Avg) = " + res.ToString());
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        //Object adaptor implementation
        private void btnObjectAdaptor_Click(object sender, EventArgs e)
        {
            try
            {
                IMathTarget imt = new MathAdapter2();
                double[] A = { 3.7, 8.4, 6.3 };
                //computing avg value
                double res = imt.ComputeAvgNew(A);
                //computing rounded avg value
                double resRndAvg = imt.ComputeAvgRound(A);
                //computing min value
                double resMin = imt.FindMinNew(A);

                MessageBox.Show("Result for avg = " + res.ToString());

                MessageBox.Show("Result for rounded avg = " + resRndAvg.ToString());

                MessageBox.Show("Result for min = " + resMin.ToString());
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void btnAdapter2Way_Click(object sender, EventArgs e)
        {
            IExistingMath im = new MathAdapterTwoWay();
            double res = im.ComputeAvg(7.3f, 6.4f, 8.5f);
            MessageBox.Show("Avg from legacy ComputeAvg = " + res.ToString());

            INewMath inm = new MathAdapterTwoWay();
            double[] Arr = { 7.3f, 6.4f, 8.5f };
            double res2 = inm.ComputeAvgNew(Arr);
            MessageBox.Show("Result from new ComputeAvg = " + res2.ToString());

        }
    }
}
