namespace TestD1
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
            cmbCategories = new ComboBox();
            dg1 = new DataGridView();
            ((System.ComponentModel.ISupportInitialize)dg1).BeginInit();
            SuspendLayout();
            // 
            // cmbCategories
            // 
            cmbCategories.FormattingEnabled = true;
            cmbCategories.Location = new Point(12, 12);
            cmbCategories.Name = "cmbCategories";
            cmbCategories.Size = new Size(151, 28);
            cmbCategories.TabIndex = 0;
            cmbCategories.SelectedIndexChanged += cmbCategories_SelectedIndexChanged;
            // 
            // dg1
            // 
            dg1.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            dg1.Location = new Point(210, 12);
            dg1.Name = "dg1";
            dg1.RowHeadersWidth = 51;
            dg1.Size = new Size(578, 426);
            dg1.TabIndex = 1;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(dg1);
            Controls.Add(cmbCategories);
            Name = "Form1";
            Text = "Products";
            Load += Form1_Load;
            ((System.ComponentModel.ISupportInitialize)dg1).EndInit();
            ResumeLayout(false);
        }

        #endregion

        private ComboBox cmbCategories;
        private DataGridView dg1;
    }
}
