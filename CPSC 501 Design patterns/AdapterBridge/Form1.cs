using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace AdapterBridge
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnTestBridge_Click(object sender, EventArgs e)
        {
            IAreaVolumeOur ic = new ComputeBridge(new AdapterLibrary1());
            double res = ic.ComputeCylinderVolume(5, 10);
            MessageBox.Show("Cyl vol = " + res.ToString());
        }
    }
}
