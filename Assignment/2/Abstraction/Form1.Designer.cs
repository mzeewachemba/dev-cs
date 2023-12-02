namespace Abstraction
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
            btnTestAreaVolume = new Button();
            btnTestIclonable = new Button();
            btnTestICloneableAddr = new Button();
            btnTestIComparable = new Button();
            SuspendLayout();
            // 
            // btnTestAreaVolume
            // 
            btnTestAreaVolume.Location = new Point(110, 28);
            btnTestAreaVolume.Name = "btnTestAreaVolume";
            btnTestAreaVolume.Size = new Size(199, 41);
            btnTestAreaVolume.TabIndex = 0;
            btnTestAreaVolume.Text = "Test Area Volume";
            btnTestAreaVolume.UseVisualStyleBackColor = true;
            btnTestAreaVolume.Click += btnTestAreaVolume_Click;
            // 
            // btnTestIclonable
            // 
            btnTestIclonable.Location = new Point(110, 75);
            btnTestIclonable.Name = "btnTestIclonable";
            btnTestIclonable.Size = new Size(199, 42);
            btnTestIclonable.TabIndex = 1;
            btnTestIclonable.Text = "Test IClonable";
            btnTestIclonable.UseVisualStyleBackColor = true;
            btnTestIclonable.Click += btnTestIclonable_Click;
            // 
            // btnTestICloneableAddr
            // 
            btnTestICloneableAddr.Location = new Point(110, 123);
            btnTestICloneableAddr.Name = "btnTestICloneableAddr";
            btnTestICloneableAddr.Size = new Size(199, 42);
            btnTestICloneableAddr.TabIndex = 2;
            btnTestICloneableAddr.Text = "Test ICloneable Addr";
            btnTestICloneableAddr.UseVisualStyleBackColor = true;
            btnTestICloneableAddr.Click += btnTestICloneableAddr_Click;
            // 
            // btnTestIComparable
            // 
            btnTestIComparable.Location = new Point(110, 171);
            btnTestIComparable.Name = "btnTestIComparable";
            btnTestIComparable.Size = new Size(199, 40);
            btnTestIComparable.TabIndex = 3;
            btnTestIComparable.Text = "Test IComparable";
            btnTestIComparable.UseVisualStyleBackColor = true;
            btnTestIComparable.Click += btnTestIComparable_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(449, 234);
            Controls.Add(btnTestIComparable);
            Controls.Add(btnTestICloneableAddr);
            Controls.Add(btnTestIclonable);
            Controls.Add(btnTestAreaVolume);
            Name = "Form1";
            Text = "Areas and Volumes";
            ResumeLayout(false);
        }

        #endregion

        private Button btnTestAreaVolume;
        private Button btnTestIclonable;
        private Button btnTestICloneableAddr;
        private Button btnTestIComparable;
    }
}