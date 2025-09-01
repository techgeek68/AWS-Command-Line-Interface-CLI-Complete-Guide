using System;
using System.Threading.Tasks;
using Amazon.EC2;
using Amazon.EC2.Model;

public class Program
{
    public static async Task Main()
    {
        using var ec2 = new AmazonEC2Client(); // Region & credentials from environment/profile
        var resp = await ec2.DescribeRegionsAsync(new DescribeRegionsRequest());
        Console.WriteLine("Regions:");
        foreach (var r in resp.Regions)
            Console.WriteLine($"- {r.RegionName}");
    }
}
