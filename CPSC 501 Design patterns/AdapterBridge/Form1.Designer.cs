namespace AdapterBridge
{
    partial class Form1
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
            this.btnTestBridge = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // btnTestBridge
            // 
            this.btnTestBridge.Location = new System.Drawing.Point(42, 67);
            this.btnTestBridge.Name = "btnTestBridge";
            this.btnTestBridge.Size = new System.Drawing.Size(197, 38);
            this.btnTestBridge.TabIndex = 0;
            this.btnTestBridge.Text = "Test Bridge";
            this.btnTestBridge.UseVisualStyleBackColor = true;
            this.btnTestBridge.Click += new System.EventHandler(this.btnTestBridge_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(298, 450);
            this.Controls.Add(this.btnTestBridge);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btnTestBridge;
    }
}

