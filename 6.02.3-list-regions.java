import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.ec2.Ec2Client;
import software.amazon.awssdk.services.ec2.model.DescribeRegionsResponse;

public class ListRegions {
    public static void main(String[] args) {
        try (Ec2Client ec2 = Ec2Client.builder()
                .region(Region.US_EAST_1) // Or omit to auto-resolve
                .build()) {
            DescribeRegionsResponse resp = ec2.describeRegions();
            resp.regions().forEach(r -> System.out.println(r.regionName()));
        }
    }
}
