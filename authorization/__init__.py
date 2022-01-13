import discord


async def check_member(ctx: discord, allowed_roles: list):
    member = ctx.me
    member_roles = set([role.name for role in member.roles])
    allowed_role = set(allowed_roles)

    if member_roles.intersection(allowed_role):
        return True

    await ctx.send("You are not allowed!")

    return False
