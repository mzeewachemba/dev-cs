namespace First
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
            btnCompute = new Button();
            SuspendLayout();
            // 
            // btnCompute
            // 
            btnCompute.Location = new Point(37, 49);
            btnCompute.Name = "btnCompute";
            btnCompute.Size = new Size(164, 29);
            btnCompute.TabIndex = 0;
            btnCompute.Text = "ComputeArea";
            btnCompute.UseVisualStyleBackColor = true;
            btnCompute.UseWaitCursor = true;
            btnCompute.Click += btnCompute_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(btnCompute);
            Name = "Form1";
            Text = "Form1";
            ResumeLayout(false);
        }

        #endregion

        private Button btnCompute;
    }
}