namespace ObserverPattern
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
            btnObserver = new Button();
            SuspendLayout();
            // 
            // btnObserver
            // 
            btnObserver.Location = new Point(47, 48);
            btnObserver.Name = "btnObserver";
            btnObserver.Size = new Size(163, 42);
            btnObserver.TabIndex = 0;
            btnObserver.Text = "Observer";
            btnObserver.UseVisualStyleBackColor = true;
            btnObserver.Click += btnObserver_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(266, 163);
            Controls.Add(btnObserver);
            Name = "Form1";
            Text = "Observer";
            ResumeLayout(false);
        }

        #endregion

        private Button btnObserver;
    }
}
