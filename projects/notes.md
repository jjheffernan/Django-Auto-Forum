# Project Model Notes

This notes file is to describe what is going on within the special projects app.
Projects are a fundamental building block of this style of forum. Without them,
the boards will only have nuance separating them from any other older ones.
Projects are designed to be embedded views, that link out to another web page.
These are going to be super built out, "build thread" style servers, ideally.

## Accessing Objects (virtual python shell)

first access Project.objects. This returns a management object:
`<django.db.models.manager.Manager object at 0x102b7f280>`

Next, construct a QuerySet via a Manager on the model class (in CLI). After,
.mutators can be applied such as `.all()` or `.get()`.

QuerySet: Represents a collection of objects from db. It can have 0, 1, or many filters.
This equates to a SELECT statement, with WHERE and LIMIT abstracted away. Commonly,
the database is managed by one or more ***Manager*** objects

Project Details would have:
- Overview table of contents
- Markdown Support 
- Embedded Images (that can be reshared elsewhere, but are routed thru here)
- rich text editor
- saving/drafts
- comments different from forum comments
- Math support (common equation format)
- Tag support for vehicles
- Unlimited Length (smart document)
- Can be posted to a vehicle or a Profile (or both?)
