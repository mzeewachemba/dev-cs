using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BuilderPattern
{
    internal class StudentsReport
    {
        public string HeaderPart { get; set; }
        public string BodyPart { get; set; } = "";
        public string ProgressPart { get; set; } = "";
        public string FooterPart { get; set; }
        //building the component
        public override string ToString() =>
        new StringBuilder()
        .AppendLine(HeaderPart)
        .AppendLine(BodyPart)
        .AppendLine(ProgressPart)
        .AppendLine(FooterPart)
        .ToString();
    }
}
