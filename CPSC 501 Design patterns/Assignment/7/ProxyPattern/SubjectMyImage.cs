using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProxyPattern
{
    internal class SubjectMyImage : ISubjectMyImage //real class
    {
        Bitmap bmp = null;
        Size sz;
        string shortName = "";
        string fileName;
        string category = "";
        public SubjectMyImage(string filename, string sName, string cat)
        {
            fileName = filename;
            category = cat;
            shortName = sName;
            //gets the bitmap and size when Image is created
            bmp = new Bitmap(Image.FromFile(filename));
            sz = new Size(bmp.Width, bmp.Height);
        }

        public string ShortName
        {
            get { return shortName; }
        }

        public string GetFileName()
        {
            return fileName;
        }
        public string Category
        {
            get { return category; }
        }

        public Bitmap GetBitmap()
        {
            return bmp;
        }
        public Size GetImageSize()
        {
            return sz;
        }
    }
}
