using System;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

class Program
{
    static async Task Main()
    {
        //privacy and security related
        var apiKey = "gsk_Edit_Your_API_Key_Here"; 

        using var client = new HttpClient();
        client.DefaultRequestHeaders.Add("Authorization", $"Bearer {apiKey}");

        var userStory = "Implement and test a simple AI C# program";

        var requestBody = new
        {
            model = "llama-3.1-8b-instant",
            messages = new[]
            {
                new
                {
                    role = "user",
                    content = $"Break this user story into 2-5 concise development tasks: {userStory}"
                }
            }
        };

        var json = JsonSerializer.Serialize(requestBody);
        var content = new StringContent(json, Encoding.UTF8, "application/json");

        var response = await client.PostAsync(
            "https://api.groq.com/openai/v1/chat/completions",
            content
        );

        var responseText = await response.Content.ReadAsStringAsync();
        Console.WriteLine("Raw response:");
        Console.WriteLine(responseText);

        if (!response.IsSuccessStatusCode)
        {
            Console.WriteLine("Request failed.");
            return;
        }

        using var doc = JsonDocument.Parse(responseText);
        var reply = doc.RootElement
            .GetProperty("choices")[0]
            .GetProperty("message")
            .GetProperty("content")
            .GetString();

        Console.WriteLine("\nTask breakdown:");
        Console.WriteLine(reply);
    }
}
