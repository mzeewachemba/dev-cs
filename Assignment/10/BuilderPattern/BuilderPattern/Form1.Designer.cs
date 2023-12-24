namespace BuilderPattern
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            btnTestGradeReport = new Button();
            btnTestProgressReport = new Button();
            SuspendLayout();
            // 
            // btnTestGradeReport
            // 
            btnTestGradeReport.Location = new Point(73, 50);
            btnTestGradeReport.Name = "btnTestGradeReport";
            btnTestGradeReport.Size = new Size(156, 46);
            btnTestGradeReport.TabIndex = 0;
            btnTestGradeReport.Text = "Test Grade Report";
            btnTestGradeReport.UseVisualStyleBackColor = true;
            btnTestGradeReport.Click += btnTestGradeReport_Click;
            // 
            // btnTestProgressReport
            // 
            btnTestProgressReport.Location = new Point(73, 167);
            btnTestProgressReport.Name = "btnTestProgressReport";
            btnTestProgressReport.Size = new Size(156, 44);
            btnTestProgressReport.TabIndex = 1;
            btnTestProgressReport.Text = "Test Progress Report";
            btnTestProgressReport.UseVisualStyleBackColor = true;
            btnTestProgressReport.Click += btnTestProgressReport_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(326, 450);
            Controls.Add(btnTestProgressReport);
            Controls.Add(btnTestGradeReport);
            Name = "Form1";
            Text = "Builder";
            Load += Form1_Load;
            ResumeLayout(false);
        }

        #endregion

        private Button btnTestGradeReport;
        private Button btnTestProgressReport;
    }
}
