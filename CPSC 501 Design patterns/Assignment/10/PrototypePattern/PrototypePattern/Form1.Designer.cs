namespace PrototypePattern
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
            btnProtoType = new Button();
            btnTestPrototypeManager = new Button();
            SuspendLayout();
            // 
            // btnProtoType
            // 
            btnProtoType.Location = new Point(73, 48);
            btnProtoType.Name = "btnProtoType";
            btnProtoType.Size = new Size(215, 45);
            btnProtoType.TabIndex = 0;
            btnProtoType.Text = "ProtoType";
            btnProtoType.UseVisualStyleBackColor = true;
            btnProtoType.Click += btnProtoType_Click;
            // 
            // btnTestPrototypeManager
            // 
            btnTestPrototypeManager.Location = new Point(73, 142);
            btnTestPrototypeManager.Name = "btnTestPrototypeManager";
            btnTestPrototypeManager.Size = new Size(215, 46);
            btnTestPrototypeManager.TabIndex = 1;
            btnTestPrototypeManager.Text = "Test Prototype Manager";
            btnTestPrototypeManager.UseVisualStyleBackColor = true;
            btnTestPrototypeManager.Click += btnTestPrototypeManager_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(381, 254);
            Controls.Add(btnTestPrototypeManager);
            Controls.Add(btnProtoType);
            Name = "Form1";
            Text = "Prototype";
            ResumeLayout(false);
        }

        #endregion

        private Button btnProtoType;
        private Button btnTestPrototypeManager;
    }
}
