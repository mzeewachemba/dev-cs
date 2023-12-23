namespace ProxyPattern
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
            cmbPictures = new ComboBox();
            lblShortName = new Label();
            lblCategory = new Label();
            btnShowImage = new Button();
            lblWidth = new Label();
            lblHeight = new Label();
            pc1 = new PictureBox();
            label1 = new Label();
            label2 = new Label();
            btnProtectionProxy = new Button();
            ((System.ComponentModel.ISupportInitialize)pc1).BeginInit();
            SuspendLayout();
            // 
            // cmbPictures
            // 
            cmbPictures.FormattingEnabled = true;
            cmbPictures.Location = new Point(155, 56);
            cmbPictures.Name = "cmbPictures";
            cmbPictures.Size = new Size(221, 28);
            cmbPictures.TabIndex = 0;
            cmbPictures.SelectedIndexChanged += cmbPictures_SelectedIndexChanged;
            // 
            // lblShortName
            // 
            lblShortName.BorderStyle = BorderStyle.FixedSingle;
            lblShortName.Location = new Point(155, 134);
            lblShortName.Name = "lblShortName";
            lblShortName.Size = new Size(221, 25);
            lblShortName.TabIndex = 1;
            // 
            // lblCategory
            // 
            lblCategory.BorderStyle = BorderStyle.FixedSingle;
            lblCategory.Location = new Point(155, 193);
            lblCategory.Name = "lblCategory";
            lblCategory.Size = new Size(221, 27);
            lblCategory.TabIndex = 2;
            // 
            // btnShowImage
            // 
            btnShowImage.Location = new Point(155, 243);
            btnShowImage.Name = "btnShowImage";
            btnShowImage.Size = new Size(221, 45);
            btnShowImage.TabIndex = 3;
            btnShowImage.Text = "Show Image";
            btnShowImage.UseVisualStyleBackColor = true;
            btnShowImage.Click += btnShowImage_Click;
            // 
            // lblWidth
            // 
            lblWidth.AutoSize = true;
            lblWidth.Location = new Point(616, 476);
            lblWidth.Name = "lblWidth";
            lblWidth.Size = new Size(0, 20);
            lblWidth.TabIndex = 4;
            // 
            // lblHeight
            // 
            lblHeight.AutoSize = true;
            lblHeight.Location = new Point(742, 476);
            lblHeight.Name = "lblHeight";
            lblHeight.Size = new Size(0, 20);
            lblHeight.TabIndex = 5;
            // 
            // pc1
            // 
            pc1.Location = new Point(392, 56);
            pc1.Name = "pc1";
            pc1.Size = new Size(706, 394);
            pc1.TabIndex = 8;
            pc1.TabStop = false;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(51, 139);
            label1.Name = "label1";
            label1.Size = new Size(49, 20);
            label1.TabIndex = 9;
            label1.Text = "Name";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(51, 200);
            label2.Name = "label2";
            label2.Size = new Size(69, 20);
            label2.TabIndex = 10;
            label2.Text = "Category";
            // 
            // btnProtectionProxy
            // 
            btnProtectionProxy.Location = new Point(155, 581);
            btnProtectionProxy.Name = "btnProtectionProxy";
            btnProtectionProxy.Size = new Size(221, 41);
            btnProtectionProxy.TabIndex = 11;
            btnProtectionProxy.Text = "Protection Proxy";
            btnProtectionProxy.UseVisualStyleBackColor = true;
            btnProtectionProxy.Click += btnProtectionProxy_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(1110, 698);
            Controls.Add(btnProtectionProxy);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(pc1);
            Controls.Add(lblHeight);
            Controls.Add(lblWidth);
            Controls.Add(btnShowImage);
            Controls.Add(lblCategory);
            Controls.Add(lblShortName);
            Controls.Add(cmbPictures);
            Name = "Form1";
            Text = "Proxy";
            Load += Form1_Load;
            ((System.ComponentModel.ISupportInitialize)pc1).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private ComboBox cmbPictures;
        private Label lblShortName;
        private Label lblCategory;
        private Button btnShowImage;
        private Label lblWidth;
        private Label lblHeight;
        private PictureBox pc1;
        private Label label1;
        private Label label2;
        private Button btnProtectionProxy;
    }
}
