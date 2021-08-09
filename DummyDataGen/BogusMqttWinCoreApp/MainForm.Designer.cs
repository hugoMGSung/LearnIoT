namespace BogusMqttWinCoreApp
{
    partial class MainForm
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
            this.label1 = new System.Windows.Forms.Label();
            this.TxtBrokerIp = new System.Windows.Forms.TextBox();
            this.BtnConnect = new System.Windows.Forms.Button();
            this.RtbLog = new System.Windows.Forms.RichTextBox();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(32, 72);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(118, 20);
            this.label1.TabIndex = 0;
            this.label1.Text = "MQTT Broker IP";
            // 
            // TxtBrokerIp
            // 
            this.TxtBrokerIp.Location = new System.Drawing.Point(168, 69);
            this.TxtBrokerIp.Name = "TxtBrokerIp";
            this.TxtBrokerIp.Size = new System.Drawing.Size(732, 27);
            this.TxtBrokerIp.TabIndex = 1;
            this.TxtBrokerIp.Text = "localhost";
            // 
            // BtnConnect
            // 
            this.BtnConnect.Location = new System.Drawing.Point(906, 67);
            this.BtnConnect.Name = "BtnConnect";
            this.BtnConnect.Size = new System.Drawing.Size(132, 29);
            this.BtnConnect.TabIndex = 2;
            this.BtnConnect.Text = "CONNECT";
            this.BtnConnect.UseVisualStyleBackColor = true;
            this.BtnConnect.Click += new System.EventHandler(this.BtnConnect_Click);
            // 
            // RtbLog
            // 
            this.RtbLog.BackColor = System.Drawing.SystemColors.InactiveBorder;
            this.RtbLog.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.RtbLog.Location = new System.Drawing.Point(23, 107);
            this.RtbLog.Name = "RtbLog";
            this.RtbLog.ScrollBars = System.Windows.Forms.RichTextBoxScrollBars.Vertical;
            this.RtbLog.Size = new System.Drawing.Size(1234, 590);
            this.RtbLog.TabIndex = 3;
            this.RtbLog.Text = "";
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1280, 720);
            this.Controls.Add(this.RtbLog);
            this.Controls.Add(this.BtnConnect);
            this.Controls.Add(this.TxtBrokerIp);
            this.Controls.Add(this.label1);
            this.MaximizeBox = false;
            this.Name = "MainForm";
            this.Resizable = false;
            this.Text = ".NET Core Mqtt Fake Publisher";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.MainForm_FormClosing);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox TxtBrokerIp;
        private System.Windows.Forms.Button BtnConnect;
        private System.Windows.Forms.RichTextBox RtbLog;
    }
}

