using Bogus;
using System;
using System.Collections.Generic;

namespace BogustTestApp
{
    public class SampleCustomerRepository
    {
        public IEnumerable<Customer> GetCustomers()
        {
            Randomizer.Seed = new Random(123456);
            var genOrder = new Faker<Order>()
                .RuleFor(o => o.Id, Guid.NewGuid)
                .RuleFor(o => o.Date, f => f.Date.Past(3))
                .RuleFor(o => o.OrderValue, f => f.Finance.Amount(5000, 150000))
                .RuleFor(o => o.Shipped, f => f.Random.Bool(0.5f));

            var genCustomer = new Faker<Customer>()
                .RuleFor(o => o.Id, Guid.NewGuid)
                .RuleFor(o => o.Name, f => f.Company.CompanyName())
                .RuleFor(o => o.Address, f => f.Address.FullAddress())
                .RuleFor(o => o.Phone, f => f.Phone.PhoneNumber("010-####-####"))
                .RuleFor(o => o.ContactName, f => f.Name.FullName())
                .RuleFor(o => o.Orders, f => genOrder.Generate(f.Random.Number(1, 2)));

            return genCustomer.Generate(10);
        }
    }
}
