<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Status.aspx.cs" Inherits="SessionManagement_.Status" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <table style="width: 60%">
                <tr>
                    <td>
                        <asp:Label runat="server" Text="Username" ID="ctl00"></asp:Label>&nbsp;</td>
                    <td>
                        <asp:Label runat="server" Text="[lblUsername]" ID="lblUsername"></asp:Label>&nbsp;</td>
                </tr>
                <tr>
                    <td>
                        <asp:Label runat="server" Text="Account Num" ID="ctl02"></asp:Label>&nbsp;</td>
                    <td>
                        <asp:Label runat="server" Text="[lblAccountNum]" ID="lblAccountNum"></asp:Label>&nbsp;</td>
                </tr>
                <tr>
                    <td>
                        <asp:Label runat="server" Text="Last Login Time" ID="ctl03"></asp:Label>&nbsp;</td>
                    <td>
                        <asp:Label runat="server" Text="[lblLastLogin]" ID="lblLastLogin"></asp:Label>&nbsp;</td>
                </tr>
                <tr>
                    <td>
                        &nbsp;</td>
                    <td>
                        <asp:Label runat="server" Text="[lblStatus]" ID="lblStatus"></asp:Label>&nbsp;</td>
                </tr>
            </table>

        </div>                
    </form>
</body>
</html>
