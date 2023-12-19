namespace FacadePattern
{
    partial class fmMortgage1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
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
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.btnMortgageApproval = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // btnMortgageApproval
            // 
            this.btnMortgageApproval.Location = new System.Drawing.Point(50, 42);
            this.btnMortgageApproval.Name = "btnMortgageApproval";
            this.btnMortgageApproval.Size = new System.Drawing.Size(213, 49);
            this.btnMortgageApproval.TabIndex = 0;
            this.btnMortgageApproval.Text = "Mortgage Approval";
            this.btnMortgageApproval.UseVisualStyleBackColor = true;
            this.btnMortgageApproval.Click += new System.EventHandler(this.btnMortgageApproval_Click);
            // 
            // fmMortgage1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.btnMortgageApproval);
            this.Name = "fmMortgage1";
            this.Text = "Mortgage Department";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btnMortgageApproval;
    }
}

