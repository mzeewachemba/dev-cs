<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="ShoppingCartCheckout.aspx.cs" Inherits="ShoppingCartDecoratorPattern.ShoppingCartCheckout" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <table style="width: 50%">
    <tr>
        <td>&nbsp;<asp:Label ID="Label1" runat="server" Text="ProductId"></asp:Label></td>
        <td>&nbsp;<asp:Label ID="Label2" runat="server" Text="Name"></asp:Label></td>
        <td>&nbsp;<asp:Label ID="Label5" runat="server" Text="Price"></asp:Label></td>
        <td>&nbsp;<asp:Label ID="Label3" runat="server" Text="Quantity"></asp:Label></td>
        <td>&nbsp;<asp:Label ID="Label4" runat="server" Text="Total"></asp:Label></td>
    </tr>
    <tr>
        <td>&nbsp;<asp:Label ID="Label11" runat="server" Text="1001"></asp:Label></td>
        <td>&nbsp;<asp:Label ID="Label14" runat="server" Text="Laptop"></asp:Label></td>
        <td>&nbsp;<asp:Label ID="Label17" runat="server" Text="799.95"></asp:Label></td>
        <td>&nbsp;<asp:TextBox runat="server" ID="txtQt1"></asp:TextBox></td>
        <td>&nbsp;<asp:Label ID="lblTotal1" runat="server" Text=""></asp:Label></td>
    </tr>
    <tr>
        <td>&nbsp;<asp:Label ID="Label12" runat="server" Text="1002"></asp:Label></td>
        <td>&nbsp;<asp:Label ID="Label15" runat="server" Text="Camera"></asp:Label></td>
        <td>&nbsp;<asp:Label ID="Label18" runat="server" Text="89.95"></asp:Label></td>
        <td>&nbsp;<asp:TextBox ID="txtQt2" runat="server"></asp:TextBox></td>
        <td>&nbsp;<asp:Label ID="lblTotal2" runat="server" Text=""></asp:Label></td>
    </tr>
    <tr>
        <td>&nbsp;<asp:Label ID="Label13" runat="server" Text="1003"></asp:Label></td>
        <td>&nbsp;<asp:Label ID="Label16" runat="server" Text="Calculator"></asp:Label></td>
        <td>&nbsp;<asp:Label ID="Label19" runat="server" Text="39.90"></asp:Label></td>
        <td>&nbsp;<asp:TextBox ID="txtQt3" runat="server"></asp:TextBox></td>
        <td>&nbsp;<asp:Label ID="lblTotal3" runat="server" Text=""></asp:Label></td>
    </tr>
    <tr>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
        <td>&nbsp;<asp:Label ID="Label10" runat="server" Text="Total"></asp:Label></td>
        <td>&nbsp;<asp:Label ID="lblGrandTotal" runat="server" Text=""></asp:Label></td>
    </tr>
    <tr>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
    </tr>
    <tr>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
        <td>&nbsp;<asp:Button ID="btnCheckout" runat="server" Text="Checkout"  OnClick="btnCheckout_Click"/></td>
        <td>&nbsp;</td>
    </tr>
    <tr>
        <td colspan="5" >&nbsp;<asp:Label ID="lblMessage" runat="server" Text=""></asp:Label></td>
    </tr>
</table>
        </div>
    </form>
</body>
</html>
