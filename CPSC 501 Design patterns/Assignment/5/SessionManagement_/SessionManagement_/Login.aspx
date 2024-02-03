<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Login.aspx.cs" Inherits="SessionManagement_.Login" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
        </div>
        <table style="width: 60%;">
            <tr>
                <td>
                    <asp:Label runat="server" Text="Please Login" ID="ctl06"></asp:Label>&nbsp;</td>
                <td>&nbsp;</td>
            </tr>
            <tr>
                <td>
                    <asp:Label runat="server" Text="Username" ID="ctl08"></asp:Label>&nbsp;</td>
                <td>
                    <asp:TextBox runat="server" ID="txtUsername"></asp:TextBox>&nbsp;</td>
            </tr>
            <tr>
                <td>
                    <asp:Label runat="server" Text="Password" ID="ctl09"></asp:Label>&nbsp;</td>
                <td>
                    <asp:TextBox runat="server" ID="txtPassword"></asp:TextBox>&nbsp;</td>
            </tr>
            <tr>
                <td>&nbsp;</td>
                <td>
                    <asp:Button runat="server" Text="Login" ID="btnLogin" OnClick="btnLogin_Click"></asp:Button>&nbsp;</td>
            </tr>
            <tr>
                <td>&nbsp;</td>
                <td>
                    <asp:Label runat="server" Text="[lblStatus]" ID="lblStatus"></asp:Label>&nbsp;</td>
            </tr>
        </table>

    </form>
</body>
</html>
