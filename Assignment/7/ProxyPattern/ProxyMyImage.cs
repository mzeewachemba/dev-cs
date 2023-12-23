using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProxyPattern
{
    internal class ProxyMyImage : ISubjectMyImage //to replace real sobject by proxy
    {
        ISubjectMyImage ism = null;
        string fileName = "";
        string shortName = "";
        string category = "";
        public ProxyMyImage(string fname, string sname, string cat)
        {
            fileName = fname;
            category = cat;
            shortName = sname;
        }
        void CreateSubject()
        {
            if (ism == null)
                ism = new SubjectMyImage(fileName, shortName, category);
        }
        public string ShortName
        {
            get
            {
                return shortName; // no need to create real subject
            }
        }
        public string Category
        {
            get
            {
                return category; // no need to create real subject
            }
        }
        public string GetFileName()
        {
            return fileName; // no need to create real subject
        }
        //needed
        public System.Drawing.Bitmap GetBitmap()
        {
            CreateSubject(); // create subject since bitmap is needed
            return ism.GetBitmap();
        }
        public System.Drawing.Size GetImageSize()
        {
            CreateSubject(); // create subject since it is needed
            return ism.GetImageSize();
        }
    }
}
