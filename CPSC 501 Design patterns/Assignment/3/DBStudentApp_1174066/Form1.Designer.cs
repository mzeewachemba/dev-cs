namespace DBStudentApp_1174066
{
    partial class fmStudent
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
            cmbCourses = new ComboBox();
            dg1 = new DataGridView();
            ((System.ComponentModel.ISupportInitialize)dg1).BeginInit();
            SuspendLayout();
            // 
            // cmbCourses
            // 
            cmbCourses.FormattingEnabled = true;
            cmbCourses.Location = new Point(32, 33);
            cmbCourses.Name = "cmbCourses";
            cmbCourses.Size = new Size(253, 28);
            cmbCourses.TabIndex = 0;
            cmbCourses.SelectedIndexChanged += cmbCourses_SelectedIndexChanged;
            // 
            // dg1
            // 
            dg1.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            dg1.Location = new Point(307, 33);
            dg1.Name = "dg1";
            dg1.RowHeadersWidth = 51;
            dg1.RowTemplate.Height = 29;
            dg1.Size = new Size(916, 356);
            dg1.TabIndex = 1;
            // 
            // fmStudent
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(1250, 450);
            Controls.Add(dg1);
            Controls.Add(cmbCourses);
            Name = "fmStudent";
            Text = "Student Form";
            Load += fmStudent_Load;
            ((System.ComponentModel.ISupportInitialize)dg1).EndInit();
            ResumeLayout(false);
        }

        #endregion

        private ComboBox cmbCourses;
        private DataGridView dg1;
    }
}