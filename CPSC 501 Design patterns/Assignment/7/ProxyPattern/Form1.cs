using System.ComponentModel;
using System.Drawing;
using System.Security.Policy;

namespace ProxyPattern
{
    public partial class Form1 : Form
    {
        //PList
        //contains objects of SubjectMyImage which further has fields for the image name, its size and the bitmap
        //belonging to the image.
        List<SubjectMyImage> PList = new List<SubjectMyImage>();
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //put images into their respective cateories and add them to the list
            cmbPictures.Items.Clear();
            string picfolder = @"D:\13.MSCS\repo__\dev-cs\Assignment\7\MyImages\Images";
            //retrieve information of images directory
            DirectoryInfo di = new DirectoryInfo(picfolder);
            //loop through the files
            foreach (FileInfo fi in di.GetFiles())
            {
                SubjectMyImage smi = new SubjectMyImage(fi.FullName, fi.Name, "Flowers");
                //populate the list with the images from the folder
                PList.Add(smi);
                //add items to combobox
                cmbPictures.Items.Add(smi.ShortName);
            }
            picfolder = @"D:\13.MSCS\repo__\dev-cs\Assignment\7\MyImages\Images2";
            di = new DirectoryInfo(picfolder);
            foreach (FileInfo fi in di.GetFiles())
            {
                SubjectMyImage smi = new SubjectMyImage(fi.FullName, fi.Name, "Mountains");
                //populate the list with the images from the folder
                PList.Add(smi);
                //add items to combobox
                cmbPictures.Items.Add(smi.ShortName);
            }
        }
        //loop through images to populate category and names
        private void cmbPictures_SelectedIndexChanged(object sender, EventArgs e)
        {
            btnShowImage.Enabled = true;
            string sname = cmbPictures.Text;
            foreach (SubjectMyImage smi in PList)
            {
                if (sname == smi.ShortName)
                {
                    //load images details to the label
                    lblCategory.Text = smi.Category;
                    lblShortName.Text = smi.ShortName;
                }
            }
        }
        //loop theough images to load image to the page and populate size
        private void btnShowImage_Click(object sender, EventArgs e) //calls the expensive operations only when btnShowImage is clicked
        {
            string sname = cmbPictures.Text;
            foreach (SubjectMyImage smi in PList)
            {
                if (sname == smi.ShortName)
                {
                    //load images
                    pc1.Image = smi.GetBitmap();
                    //load its details
                    lblWidth.Text = smi.GetImageSize().Width.ToString();
                    lblHeight.Text = smi.GetImageSize().Height.ToString();
                }
            }
        }

        private void btnProtectionProxy_Click(object sender, EventArgs e)
        {
            try
            {
                ProtectionProxy prp = new ProtectionProxy();
                bool res = prp.Authenticate("secret"); //authenticate using secret password
                string sql = "select ProductName from Products where " + "ProductId=1001";
                object obj = prp.GetSingleAnswer(sql);
                if (obj != null)
                    MessageBox.Show(obj.ToString());
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }
    }
}
