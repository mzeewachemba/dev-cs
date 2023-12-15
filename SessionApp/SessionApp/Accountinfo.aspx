
<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Accountinfo.aspx.cs" Inherits="SessionApp.Accountinfo" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <asp:Label ID="LblName" runat="server" Text="Name:"></asp:Label>
            <asp:TextBox ID="txtName" runat="server"></asp:TextBox>
            <br />
            <br />
            <asp:Label ID="LblBalance" runat="server" Text="Balance:"></asp:Label>
            <asp:TextBox ID="txtBalance" runat="server"></asp:TextBox>
            <br />
            <br />
            <asp:Label ID="lblSessioninfo" runat="server"></asp:Label>
        </div>
    </form>
</body>
</html>
