clear;close all
mu_data=1;
sg_data=.5;
noise=0.05;
x=[-0.5:0.1:2.5];
PDF=@(x,mu,sigma) (1/(sigma*sqrt(2*pi)))*exp(-((x-mu).^2)/(2*sigma^2));
y_data=PDF(x,mu_data,sg_data)+noise*randn(size(x));
y_fit=PDF(x,mu_data,sg_data);
r_fit=y_fit-y_data;
S_fit=sum(r_fit.^2);
x_range=[-1:0.1:3];
dd=@(x,y,mu,sigma) (sqrt(2/pi)*exp(-((x-mu).^2)/(2*sigma^2))).*...
    (y-(1/(sigma*sqrt(2*pi)).*exp(-((x-mu).^2)/(2*sigma^2))));
dS_dmu=@(x,y,mu,sigma) -sum(...
    ((x-mu)/sigma^3).*...
    dd(x,y,mu,sigma));
dS_dsg=@(x,y,mu,sigma) -sum(...
    (((x-mu).^2-sigma^2)/sigma^4).*...
    dd(x,y,mu,sigma));



mu_0=mu_data;
sg_0=sg_data;
J_0=[dS_dmu(x,y_data,mu_0,sg_0),dS_dsg(x,y_data,mu_0,sg_0)];

mu_3=1.6;
sg_3=1.1;
mu_2=-.2;
sg_2=.65;
mu_1=.7;
sg_1=.8;

J_1=[dS_dmu(x,y_data,mu_1,sg_1),dS_dsg(x,y_data,mu_1,sg_1)];
J_2=[dS_dmu(x,y_data,mu_2,sg_2),dS_dsg(x,y_data,mu_2,sg_2)];
J_3=[dS_dmu(x,y_data,mu_3,sg_3),dS_dsg(x,y_data,mu_3,sg_3)];

S_fun = @(mu,sg) sum((y_data-PDF(x,mu,sg)).^2);

%% Plotting
Fig=figure(...
    'Units','normalized',...
    'Position',[.33 .5 .63 .4],...
    'Color',[1 1 1],...%    'renderer','painters',...
    'WindowStyle','normal',...
    'PaperPositionMode','auto',...
    'PaperOrientation','landscape');
subplot(1,2,1);
hold on
h=plot(x,y_data,'x','markersize',8,'linewidth',2,'color',[0,0,0]);
for i=1:length(x)
    plot([x(i) x(i)], [y_data(i) PDF(x(i),mu_data,sg_data)],'k')
    % plot([x(i) x(i)], [y_data(i) mu_1*x(i)+sg_1],'r')
end
plot(x_range,PDF(x_range,mu_0,sg_0),'k:','linewidth',2);
plot(x_range,PDF(x_range,mu_1,sg_1),'r:','linewidth',2);
plot(x_range,PDF(x_range,mu_2,sg_2),'g:','linewidth',2);
plot(x_range,PDF(x_range,mu_3,sg_3),'b:','linewidth',2);
xlim([x_range(1),x_range(end)])
ylim([0,1])
hold off
set(gca,'TickLabelInterpreter','latex',...
    'LineWidth',1.2,...
    'FontSize',16);
xlabel('$x$','Interpreter','latex');
ylabel('$f(x)$','Interpreter','latex');
axis square
box
leg=legend('Data','Residuals', 'location','northwest');
set(leg,'interpreter','latex')

subplot(1,2,2);
mus=-1:0.1:3;
sgs=0.1:0.1:2;
[M,C]=meshgrid(mus,sgs);
axis square
for j=1:length(mus)
    for i=1:length(sgs)
        S(i,j)=S_fun(M(i,j),C(i,j));
    end
end
contourf(M,C,log(S),10)
colormap(flipud(pink));%flipud
xlabel('$\mu$','Interpreter','latex');
ylabel('$\sigma$','Interpreter','latex');
set(gca,'TickLabelInterpreter','latex',...
    'LineWidth',1.2,...
    'FontSize',16)
hold on
arrowscale=1/8;
plot(mu_0,sg_0,'*','markersize',12,'linewidth',2,'color',[0,0,0]);
plot(mu_1,sg_1,'*','markersize',12,'linewidth',2,'color',[1,0,0]);
quiver(mu_1,sg_1,-J_1(1)*arrowscale,-J_1(2)*arrowscale,...
    'markersize',12,'linewidth',2,'color',[1,0,0],'MaxHeadSize',.9);
plot(mu_2,sg_2,'*','markersize',12,'linewidth',2,'color',[0,1,0]);
quiver(mu_2,sg_2,-J_2(1)*arrowscale,-J_2(2)*arrowscale,...
    'markersize',12,'linewidth',2,'color',[0,1,0],'MaxHeadSize',.7);
plot(mu_3,sg_3,'*','markersize',12,'linewidth',2,'color',[0,0,1]);
quiver(mu_3,sg_3,-J_3(1)*arrowscale,-J_3(2)*arrowscale,...
    'markersize',12,'linewidth',2,'color',[0,0,1],'MaxHeadSize',2);
hold off
xlim([mus(1),mus(end)]);
ylim([sgs(1),sgs(end)]);

colo=colorbar;
set(colo,'FontSize',16, 'TickLabelInterpreter','latex')
ylabel(colo,'log($S$)','Interpreter','latex')